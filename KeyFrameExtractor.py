import cv2
import numpy as np
import re

import os
system = os.name
if system == 'nt':
    print("This is a Windows system.")
    os.environ['OMP_NUM_THREADS'] = '6'
elif system == 'posix':
    print("This is a POSIX system (likely Linux or Unix).")
else:
    print("Unknown operating system.")
    exit()

from sklearn.cluster import KMeans
from collections import Counter

import json

class KeyFrameExtractor:
    def __init__(self, video_path, video_vtt_path, extracted_dir_path, keyframes_PerMin = 8):
        self.video_path = video_path
        self.video_vtt_path = video_vtt_path
        self.extracted_dir_path = extracted_dir_path
        self.keyframes_PerMin = keyframes_PerMin

        os.makedirs(self.extracted_dir_path, exist_ok=True)
    
    def extract_features(self, frame):
        hist = cv2.calcHist([frame], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        hist = cv2.normalize(hist, hist).flatten()
        return hist
    
    def process_Path(self):
        basename = os.path.basename(self.video_path)
        root, _ = os.path.splitext(basename)
        
        full_extracted_dir_path = os.path.join(self.extracted_dir_path, root)
        extracted_frame_path = os.path.join(full_extracted_dir_path, "keyframes")
        
        if system == 'nt':
            self.video_path = self.video_path.replace("/", "\\")
            self.video_vtt_path = self.video_vtt_path.replace("/", "\\")  
            self.extracted_dir_path = extracted_frame_path.replace("/", "\\")
        elif system == 'posix':
            self.video_path = self.video_path.replace("\\", "\/")
            self.video_vtt_path = self.video_vtt_path.replace("\\", "\/")
            self.extracted_dir_path = extracted_frame_path.replace("\\", "\/")
        else:
            print("Unknown operating system.")
            exit()

        os.makedirs(self.extracted_dir_path, exist_ok=True)
        print(self.video_path)
        print(self.video_vtt_path)
        print(self.extracted_dir_path)

    def extract_keyframe(self):
        self.process_Path()

        cap = cv2.VideoCapture(self.video_path)
        if not cap.isOpened():
            raise Exception("Error: Could not open video.")

        fps = cap.get(cv2.CAP_PROP_FPS)
        frames_per_minute = int(fps * 60)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        total_minutes = total_frames // frames_per_minute
        FrameVtt = []
        subtitles = self.parse_vtt()

        for minute in range(total_minutes):
            # Reset lists for each minute
            frame_features = []
            frame_list = []

            start_frame = minute * frames_per_minute
            end_frame = start_frame + frames_per_minute

            # print(end_frame)

            cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

            while cap.get(cv2.CAP_PROP_POS_FRAMES) < end_frame:
                ret, frame = cap.read()
                if not ret:
                    break
                features = self.extract_features(frame)
                frame_features.append(features)
                frame_list.append(frame)

            kmeans = KMeans(n_clusters=self.keyframes_PerMin, n_init=10)
            kmeans.fit(frame_features)

            labels = kmeans.labels_
            key_frame_ids = []
            for i in range(self.keyframes_PerMin):
                indices = [idx for idx, label in enumerate(labels) if label == i]
                if indices:
                    cluster_center = kmeans.cluster_centers_[i]
                    distances = [np.linalg.norm(frame_features[idx] - cluster_center) for idx in indices]
                    key_frame_ids.append(indices[np.argmin(distances)])

            for frame_id in key_frame_ids:
                frame = frame_list[frame_id]
                real_frame_id = start_frame + frame_id
                save_path = os.path.join(self.extracted_dir_path, f'keyframe_{real_frame_id}.jpg')
                self.match_FrameVtt(subtitles, real_frame_id, f'keyframe_{real_frame_id}.jpg', fps, FrameVtt)
                cv2.imwrite(save_path, frame)

        cap.release()

        FrameVtt_json = [list(item) for item in FrameVtt]
        json_path = save_path = os.path.join(self.extracted_dir_path, f'frameVtt.json')
        with open(json_path, 'w') as file:
            json.dump(FrameVtt_json, file, indent=4)

        print(f"Saved key frames in folder: {self.extracted_dir_path}")

    
    def match_FrameVtt(self, subtitles, real_frame_id, real_name, fps, FrameVtt):
        realtime = real_frame_id / fps
        for tuple in subtitles:
            if realtime > tuple[0]:
                FrameVtt.append((real_name, tuple[2]))
            subtitles.remove(tuple)


    def convert_to_seconds(self, time_str):
        seconds = 0
        times = time_str.split(':')
        for i in range(len(times)):
            time = float(times[len(times) -i -1])
            time_base = 60 ** i
            seconds = seconds + float(time * time_base)
        return seconds

    def parse_vtt(self):
        with open(self.video_vtt_path, 'r', encoding='utf-8') as file:
            content = file.read()

        subtitle_regex = re.compile(r'(\d{2}:\d{2}\.\d{3}) --> (\d{2}:\d{2}\.\d{3})\n(.*?)\n\n')

        subtitles = []
        
        matches = subtitle_regex.finditer(content)

        for match in matches:
            start_time, end_time, subtitle_text = match.groups()

            start_seconds = self.convert_to_seconds(start_time)
            end_seconds = self.convert_to_seconds(end_time)

            subtitles.append((start_seconds, end_seconds, subtitle_text.replace('\n', '')))

        return subtitles

# kfe = KeyFrameExtractor("c:\Current\CS4824_project_test\Movie\M3GAN.mkv", "c:\Current\CS4824_project_test\Movie\M3GAN.vtt", "./keyframe")
kfe = KeyFrameExtractor("c:/Current/CS4824_project_test/Movie/Nobody.mkv", "c:/Current/CS4824_project_test/Movie/Nobody.vtt", "./keyframe")
# kfe = KeyFrameExtractor("c:/Current/CS4824_project_test/Movie/M3GAN.mkv", "c:/Current/CS4824_project_test/Movie/M3GAN.vtt", "./keyframe")

# kfe.extract_keyframe()