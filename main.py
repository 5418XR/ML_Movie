# import base64
# import openai
# import os

# # OpenAI API Key
# api_key = "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"

# # Function to encode the image
# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

# # Initialize OpenAI client
# openai.api_key = api_key

# # Path to your specific image
# image_path = "keyframes1\keyframe_2_0205.png"

# # Getting the base64 string
# base64_image = encode_image(image_path)

# response = openai.ChatCompletion.create(
#     model="gpt-4-vision-preview",
#     messages=[
#       {
#         "role": "user",
#         "content": [
#           {
#             "type": "text",
#             "text": "In this keyframe from the movie 'Titanic', based on the subtitle content 'Subtitle Content', what is the spatial relationship between the characters and between the characters and their environment? Describe how they interact with each other in space and how this relates to the dialog or narration in the credits. If there are no characters what are the main visual elements of this screenshot? Please analyze how these elements work together to convey content related to a specific scene or emotion in the film. Which elements are located in the foreground and which in the background in this particular scene? How does this layout enhance or reflect a particular plot point in the movie?"
#           },
#           {
#             "type": "image_url",
#             "image_url": {
#               "url": f"data:image/png;base64,{base64_image}"
#             }
#           }
#         ]
#       }
#     ],
#     max_tokens=1000
# )

# print(response.choices[0].message['content'])


import base64
import requests

# OpenAI API Key
api_key = "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"

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "C:\ml2\ML_Movie\keyframes1\keyframe_1_0150.png"

# Getting the base64 string
base64_image = encode_image(image_path)

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "What’s in this image?"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": f"data:image/jpeg;base64,{base64_image}"
            }
          }
        ]
      }
    ],
    "max_tokens": 300
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

print(response.json())


# import base64
# import openai
# import os

# # Function to read and extract a specific subtitle from an SRT file
# def extract_subtitle(srt_file_path, subtitle_number):
#     with open(srt_file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#         subtitles = content.split('\n\n')
#         if subtitle_number <= len(subtitles):
#             return subtitles[subtitle_number - 1].split('\n', 2)[2]
#         else:
#             return "Subtitle not found."

# # Load OpenAI API Key from environment variable
# api_key = "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"

# # Function to encode the image
# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

# # Initialize OpenAI client
# openai.api_key = api_key

# # Path to your specific image
# image_path = "keyframes1\\keyframe_2_0205.png"  # Ensure this path is correct

# # Path to your SRT file
# srt_file_path = "tt0120338.srt"

# # Extract the second subtitle
# subtitle_content = extract_subtitle(srt_file_path, 2)

# # Getting the base64 string
# base64_image = encode_image(image_path)

# response = openai.ChatCompletion.create(
#     model="gpt-4-vision-preview",
#     messages=[
#       {
#         "role": "user",
#         "content": [
#           {
#             "type": "text",
#             "text": f"In this keyframe from the movie 'Titanic', based on the subtitle content '{subtitle_content}', what is the spatial relationship between the characters and between the characters and their environment? Describe how they interact with each other in space and how this relates to the dialog or narration in the credits. If there are no characters what are the main visual elements of this screenshot? Please analyze how these elements work together to convey content related to a specific scene or emotion in the film. Which elements are located in the foreground and which in the background in this particular scene? How does this layout enhance or reflect a particular plot point in the movie?"
#           },
#           {
#                 "type": "image_url",
#                 "image_url": {
#                 "url": f"data:image/png;base64,{base64_image}"
#             }
#           }
#         ]
#       }
#     ],
#     max_tokens=1000
# )

# print(response.choices[0].message['content'])
# import re
# import os
# import base64
# import openai

# def format_time_for_filename(time_str):
#     # 将时间格式从 "00:01:50,903" 转换为 "0150"
#     return time_str[3:5] + time_str[6:8]

# def extract_subtitles(srt_file_path):
#     with open(srt_file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#         pattern = re.compile(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> \d{2}:\d{2}:\d{2},\d{3}\n([\s\S]+?)(?=\n\n|\Z)')
#         return pattern.findall(content)

# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

# # Load OpenAI API Key from environment variable
# api_key = "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"

# # Initialize OpenAI client
# openai.api_key = api_key

# # Path to your SRT file
# srt_file_path = "tt0120338.srt"

# # Base path to your keyframes
# base_image_path = "C:\\Users\\12146\\OneDrive\\桌面\\ml2\\ML_Movie\\keyframes1"

# # Extract subtitles
# subtitles = extract_subtitles(srt_file_path)

# for number, start_time, content in subtitles:
#     formatted_start_time = format_time_for_filename(start_time)
#     # 更新文件名格式以匹配您的文件命名约定
#     image_filename = f"keyframe_{number}_{formatted_start_time}.png"
#     image_path = os.path.join(base_image_path, image_filename)

#     if os.path.exists(image_path):
#         base64_image = encode_image(image_path)
#         response = openai.ChatCompletion.create(
#             model="gpt-4-vision-preview",
#             messages=[
#               {
#                 "role": "user",
#                 "content": [
#                   {
#                     "type": "text",
#                     "text": f"In this keyframe from the movie 'Titanic', based on the subtitle content '{content}', what is the spatial relationship between the characters and between the characters and their environment? Describe how they interact with each other in space and how this relates to the dialog or narration in the subtitles. If there are no characters what are the main visual elements of this screenshot? Please analyze how these elements work together to convey content related to a specific scene or emotion in the film. Which elements are located in the foreground and which in the background in this particular scene? How does this layout enhance or reflect a particular plot point in the movie?"
#                   },
#                   {
#                     "type": "image_url",
#                     "image_url": {
#                       "url": f"data:image/png;base64,{base64_image}"
#                     }
#                   }
#                 ]
#               }
#             ],
#             max_tokens=1000
#         )

#         # 输出或保存响应
#         print(f"Keyframe {number}: {response.choices[0].message['content']}")
#     else:
#         print(f"Image not found for keyframe {number}")

# import re
# import os
# import base64
# import openai

# def format_time_for_filename(time_str):
#     # 将时间格式从 "00:01:50,903" 转换为 "0150"
#     return time_str[3:5] + time_str[6:8]

# def extract_subtitles(srt_file_path):
#     with open(srt_file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#         pattern = re.compile(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> \d{2}:\d{2}:\d{2},\d{3}\n([\s\S]+?)(?=\n\n|\Z)')
#         return pattern.findall(content)

# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

# # Load OpenAI API Key
# api_key = "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"

# # Initialize OpenAI client
# openai.api_key = api_key

# # Path to your SRT file
# # Path to your SRT file
# srt_file_path = r"C:\ml2\ML_Movie\tt0120338.srt"


# # Base path to your keyframes
# base_image_path = r"C:\ml2\ML_Movie\keyframes1"

# # Extract subtitles
# subtitles = extract_subtitles(srt_file_path)

# # 文件用于保存结果
# results_file = "analysis_results.txt"

# with open(results_file, "w", encoding='utf-8') as file:
#     for number, start_time, content in subtitles:
#         formatted_start_time = format_time_for_filename(start_time)
#         image_filename = f"keyframe_{number}_{formatted_start_time}.png"
#         image_path = os.path.join(base_image_path, image_filename)

#         if os.path.exists(image_path):
#             base64_image = encode_image(image_path)
#             response = openai.ChatCompletion.create(
#                 model="gpt-4-vision-preview",
#                 messages=[
#                   {
#                     "role": "user",
#                     "content": [
#                       {
#                         "type": "text",
#                         "text": f"In this keyframe from the movie 'Titanic', based on the subtitle content '{content}', what is the spatial relationship between the characters and between the characters and their environment? Describe how they interact with each other in space and how this relates to the dialog or narration in the subtitles. If there are no characters what are the main visual elements of this screenshot? Please analyze how these elements work together to convey content related to a specific scene or emotion in the film. Which elements are located in the foreground and which in the background in this particular scene? How does this layout enhance or reflect a particular plot point in the movie?"
#                       },
#                       {
#                         "type": "image_url",
#                         "image_url": {
#                           "url": f"data:image/png;base64,{base64_image}"
#                         }
#                       }
#                     ]
#                   }
#                 ],
#                 max_tokens=1000
#             )

#             # 将响应写入文件
#             file.write(f"Keyframe {number}: {response.choices[0].message['content']}\n\n")
#         else:
#             print(f"Image not found for keyframe {number}")

# print(f"Analysis complete. Results saved to {results_file}")

# import re
# import os
# import base64
# import openai
# from openai import OpenAI

# def format_time_for_filename(time_str):
#     # 将时间格式从 "00:01:50,903" 转换为 "0150"
#     return time_str[3:5] + time_str[6:8]

# def extract_subtitles(srt_file_path):
#     with open(srt_file_path, 'r', encoding='utf-8') as file:
#         content = file.read()
#         pattern = re.compile(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> \d{2}:\d{2}:\d{2},\d{3}\n([\s\S]+?)(?=\n\n|\Z)')
#         return pattern.findall(content)

# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

# # Load OpenAI API Key
# api_key = "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"

# # Initialize OpenAI client
# openai.api_key = api_key

# # Path to your SRT file
# srt_file_path = r"C:\ml2\ML_Movie\tt0120338.srt"

# # Base path to your keyframes
# base_image_path = r"C:\ml2\ML_Movie\keyframes1"

# # Extract subtitles
# subtitles = extract_subtitles(srt_file_path)

# # 文件用于保存结果
# results_file = "analysis_results.txt"

# with open(results_file, "w", encoding='utf-8') as file:
#     for number, start_time, content in subtitles:
#         formatted_start_time = format_time_for_filename(start_time)
#         image_filename = f"keyframe_{number}_{formatted_start_time}.png"
#         image_path = os.path.join(base_image_path, image_filename)

#         if os.path.exists(image_path):
#             base64_image = encode_image(image_path)
#             response = openai.ChatCompletion.create(
#                 model="gpt-4-vision-preview",
#                 prompt=f"In this keyframe from the movie 'Titanic', based on the subtitle content '{content}', what is the spatial relationship between the characters and between the characters and their environment? Describe how they interact with each other in space and how this relates to the dialog or narration in the subtitles. If there are no characters what are the main visual elements of this screenshot? Please analyze how these elements work together to convey content related to a specific scene or emotion in the film. Which elements are located in the foreground and which in the background in this particular scene? How does this layout enhance or reflect a particular plot point in the movie? {base64_image}",
#                 max_tokens=1000
#             )

#             # 将响应写入文件
#             file.write(f"Keyframe {number}: {response.choices[0].text}\n\n")
#         else:
#             print(f"Image not found for keyframe {number}")

# print(f"Analysis complete. Results saved to {results_file}")
