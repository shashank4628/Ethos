import json
from .yt_extractor import get_video_info, get_audio_url
from .speech import save_transcript




# def save_video_sentiments(url):
#     video_info = get_video_info(url)
#     url = get_audio_url(video_info)
#     if url:
#         title = video_info['title']
#         title = title.strip().replace(" ", "_") 
#         title = "data/" + title
#         save_transcript(url, title, sentiment_analysis=True)
#         return title
# def printAnalysis(request,url):  
#     try:
#       fileName=save_video_sentiments(url)
#       with open(fileName+"_sentiments.json", "r") as f:
#           data = json.load(f)
          
#     except Exception as e:
#           print(f"An error occurred: {e}")


#     positives = []
#     negatives = []
#     neutrals = []
#     for result in data:
#         text = result["text"]
#         if result["sentiment"] == "POSITIVE":
#             positives.append(text)
#         elif result["sentiment"] == "NEGATIVE":
#             negatives.append(text)
#         else:
#             neutrals.append(text)
        
#     n_pos = len(positives)
#     n_neg  = len(negatives)
#     n_neut = len(neutrals)

#     print("Num positives:", n_pos)
#     print("Num negatives:", n_neg)
#     print("Num neutrals:", n_neut)

#     # ignore neutrals here
#     rp = n_pos / (n_pos + n_neg)
#     rn=n_neg/(n_neg+n_pos)
#     print(f"Positive ratio: {rp:.3f}")
#     print(f"Negative ratio: {rn:.3f}")
#     if rn >0.8:
#         print(f"This is a hate speech")



def save_video_sentiments(request,url):
    video_info = get_video_info(url)
    url = get_audio_url(video_info)
    if url:
        title = video_info['title']
        title = title.strip().replace(" ", "_")
        Title=title
        title = "data/" + title
        save_transcript(request,url, title, sentiment_analysis=True)
        return Title

def printAnalysis(request,url):
     
      save_video_sentiments(request,url)
      
    #   with open("data/"+fileName+"_sentiments.json", "r") as f:
    #     data = json.load(f)
    # except Exception as e:
    #     print(e)
     
    
    # positives = []
    # negatives = []
    # neutrals = []
    # for result in data:
    #     text = result["text"]
    #     if result["sentiment"] == "POSITIVE":
    #         positives.append(text)
    #     elif result["sentiment"] == "NEGATIVE":
    #         negatives.append(text)
    #     else:
    #         neutrals.append(text)
        
    # n_pos = len(positives)
    # n_neg  = len(negatives)
    # n_neut = len(neutrals)

    # print("Num positives:", n_pos)
    # print("Num negatives:", n_neg)
    # print("Num neutrals:", n_neut)

    # # ignore neutrals here
    # r = n_pos / (n_pos + n_neg)
    # print(f"Positive ratio: {r:.3f}")