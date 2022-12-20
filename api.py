import requests

# Make a GET request to the API
TOKEN = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..ODyme_UpJ9DrHvJR.MYWig16EbrsQbby28bzO8jVrwxXa0_y2wlYNJ_OuaT163R7oAn3XDVqCKAcEAtIS1FSwNpnL_CCihk_NJ_GRHhXk7jVTOK9hPzUeAoRc39PeoAL9WgJ-HLdnIa-RYw47zu-64ubTnJn49PVf1Iu3kFGAu20kBqdavzz8jaiaQfRG-dptdYzcxqOIjKzV43T2f2ZJm6TC6GJO-QIhKrS3XGP5RmPMMhcXJNEGL-HQRq8T3mIVTgh1is_cw1elrZfIIt2Fwk98543uywcTjRnZYwZi08x0JHYhru5bKh5VUKsazGin0_g_poO9NTciuUHB2RE26_LtwdXIIOR7UdovZCOXPeBK6Qfm94MoeK7goqy0Rv3baey2Fo7ZRdmrQxd8O4xan-Yt4bfJh171Y7Ab9oV9GMpcJ1PGrr8l7p4r7tiduyJqmvwQ9Al9aTz5ii-l3gTePcQ7qcGR3L_IishUkvaPgg6nUB1zbvlXcWVVae6C8buwQkWx2bKcpVzlJ3lBg0_RU3vu6ivzd9LeyjQEXqLk4j8SrHQQ22VcUfhhm1_8g_T3AFbJ5T2CJL9n0DYnzTqsHyvLzoXzQZLNPDH0_jo4NiovX9rxdvbPLx58ER0O7NQ3dxxsFgYXD7FCZOOxSKgQyblfxIehaS0kBq0lPZ32V7VPlDylBux-OKO8H-bfhavTGVtTusDvf_l3TjKBDFcBMoDk038l_TDOlYpDIUKseuwBQ8b2T7lxAkhu2FrT1iwizO-KuvnuH_mIGZyJFk_Ye4xQCLD9GWLizIDHkDOHbIXX1xSDEuGw4rIAhiRDE2eN_3pPwMMB7VYivBpCzG830SxKWvFVHByL8-JjiO5_r2sQc866Za8goQJMMT-9kodPmJqCVfOMJrZPuL6QX4VEhWkK84N7akuaDRzHhw0oOXgK3cw1XRbg7aHdQoPSFralTkPaJKl9ZDbYMMmrnTUNYyL9eAy6crJWqFQgnCvvgbdJ9uoOa2FiGNzUrpZ2hzfboFgRNMyxRFCptv3qj9U7gc_bGqX76QWJPCBt67FCnz7wMQW8rs0Z97Cg1IKMcC2TGeCTsa8fxkN5iG2BuNrq6w3tyJk2pp6rh763b_fqnRDRu_kk4Zt9oYZCkEiA61MNstJePv_sfR2p2i9o6CTr-KKKlV3i_0Nk4vKQjH5BDIWCAaZpW2XKvGFy01LLnjrR6K7TIwS6GYKkWS2hHQwleHQeRq-lDDKa9GkpgsG1kvpRET6_VN4BNW2lnSEH7C9wgHEveAIJWb5UkBPmo9q0VropyTTYdn5HEkAhpXOL3UYkDpdUFiLV27gLZs2kKW-W--kr151Inw3IafrEuj3x-LhtQK_WayAeSJy7c-u1ZQVggSt1gck5ctVO1fLHDNWBBwd2WsUax_K56c-OwJGaS1U2lPAOHh5eHjjkUlgWlniKV6YmUPCrvOCnahrIjPDpTy3TBloHqI2gnxQk7vFUmV7_lh-W4ybPPCPb0esX9iGzHy0c04pg_n2bWr3KWBZrmOn0JDNMlOEzuKChOjB3ZFzV_o20shOkSoRkHW-OKr87FRQSRmpeGCPGrPdAU4zJTzGWzYDgqNAiba7IxXIMj4MSJQRRYH8023EowPTamR2jkDXbKeymhg_HjCd4zoY-RNljK3DKH6OxO1SzoCRXvZcCx4Qy_zh8vr3MLhzVmvzpWJFU_aN5QviRw3YfKN7z_WecYqiNMW5YsflD2n6j42_pBjB0M92Zk1KWb8bfdzepR3ZXlkipFGT4zte46jwq9jLbyL7O1HNKv9NLJzrqy2zUdnY3niuOHRcGJa-KIuI5N13jp6anJH7sJLMfT1djUnIQAQcUvGtKZHOWWKAoc4I8JmTJzeRwTKivR2MG62aOu2vMDSwgw5LtBNDEab_Xf_-3QrRX1DSJOpolO8Vso4m3PaeOrqr-oNXP1YMe1iB3M47FLwJeVXbxZSJIFBTqtLLVCODuCTuoCcMDt7fa0bWlytbNGJAUEFAz9KhGOQrYx9a7E7gqTau7FzUg3So32kZ3SQu2E0CpmAezuoQvSjfVZdOgJ1GcebDplcKI65tFvkl05DpB-JqZrv_m-8BHLgtQEN43WigKx-htgBwSTeVBPF761LAHvCYtW-OXhhnSbQZGJ124s92gE-ec6SepAFFbeBSZCmmGOuQRcuIT9RwtcHXKeaEpe72HAWpN3_MSw5xKZNHAA9X-AfUj6mTz3U7Coot430tIlvcchQEL8sJO-ET3RkQjNUK1brtfmfuNPsr_1T12VI5NtriakKD6eDYzkkStr_SPeE0LUsfqN6tXMT8jMTpCDcT5OttLuNDG-BXRo3_ftl5gcA.ze1x_vRWPYcWwvaw6aDHtQ"
url = "https://justbrowse.io"
chatgptid = "y3EgwzUSGlpKcMYp1gCJj"
conversationidglobal =""
def connectochatgpt():
    response = requests.get(url + "/api/chatgpt/connect?sessionToken=" + TOKEN)
    if response.status_code == 200:
        #OK
        global chatgptid
        chatgptid = response.json()["id"]
        return response.json()
    else:
    # If the request was not successful, return an error message
        return {"error": "An error occurred while retrieving data from the API"}

def isready(id):
    response = requests.get(url + "/api/chatgpt/status?id=" + id)
    return response.json()["status"]

def reset():
    response = requests.get(url + "/api/chatgpt/chat/"+chatgptid+"/reset?conversationId=" + conversationidglobal)
    chatgptid = response.json()["id"]

    return response.json()["id"]

def sendmessage(message,chatgptid,conversationid):
    data = {"message": message,"conversation_id":conversationid}
    response = requests.post(url + "/api/chatgpt/chat/" + chatgptid,json=data)
        #OK
    global conversationidglobal
    #print(response.json())
    conversationidglobal = response.json()["conversationId"]
    return response.json()["reply"][0]
    # If the request was not successful, return an error message


#response = requests.get("https://justbrowse.io/api/chatgpt/status?id=y3EgwzUSGlpKcMYp1gCJj")
#answer = requests.post("https://justbrowse.io/api/chatgpt/chat/y3EgwzUSGlpKcMYp1gCJj",json=data)

# Get the status code of the response
#status_code = response.status_code

# Get the content of the response (the data returned by the API)
#dataresponse = answer.json()
#dataresponse = sendmessage("hello",chatgptid,conversationidglobal)

while True:
  response = input("Enter something (enter 'q' to quit): ")
  dataresponse = sendmessage(response,chatgptid,conversationidglobal)
  
  if response == 'q':
    break
  else:
    print("answer is : ", dataresponse)


#print(dataresponse)