import cv2
import socketio
import json
from fastapi import FastAPI

from av import VideoFrame

from aiortc import RTCPeerConnection, RTCSessionDescription, RTCIceCandidate
from aiortc.contrib.media import MediaRelay
from video_track import VideoTransformTrack

pc = RTCPeerConnection()

app = FastAPI()

sio=socketio.AsyncServer(cors_allowed_origins='*', async_mode='asgi')

socket_app = socketio.ASGIApp(sio)
app.mount("/", socket_app)

relay = MediaRelay()

@pc.on("datachannel")
def on_datachannel(**args):
    print("on_datachannel: ", args)
            
@pc.on("connectionstatechange")
def on_connectionstatechange(**args):
    print("on_connectionstatechange:", args)
                
@pc.on("icecandidate")
def on_icecandidate():
    print("on_icecandidate")

@pc.on("track")
async def track(track):
    print("track: ", track)
    if track.kind == "video":
        print("addTrack")
        pc.addTrack(VideoTransformTrack(relay.subscribe(track)))
        # pc.addTrack(track)
        
@pc.on('icegatheringstatechange')
async def on_icegatheringstatechange():
    print('ICE gathering state changed to', pc.iceGatheringState)
    if pc.iceGatheringState == 'complete':
        print('All ICE candidates have been gathered.')

@sio.on("connect")
async def connect(sid, env):
    print("new connect", str(sid))


@sio.on("msg")
async def connect(sid, env):
    print("New Client Connected to This id :"+" "+str(sid))
    
@sio.on("createStream")
async def create_stream(sid, second):
    print("create_stream: ", sid)
    await sio.emit("signal", {"type": "answer"})
    
# @sio.on("offer")
# async def offer(request, second):
#     params = second
#     offer = RTCSessionDescription(sdp=params['sdp'], type=params['type'])
        
#     await pc.setRemoteDescription(offer)
#     answer = await pc.createAnswer()
#     await pc.setLocalDescription(answer)
    
#     @pc.on("track")
#     async def on_track(track):
#         print("Track received:", track)
#         print("asd1")
#         VideoTransformTrack(track)
#         print("asd2")
        # if track.kind == "video":
        #     print("video")
        # try:
        #     frame = await track.recv()
        #     print("frame: ", frame)
        #     video_frame = frame.to_ndarray(format="bgr24")
        # except:
        #     print("Error: ")
        # print("end")

        # Відображення кадру за допомогою OpenCV
        # cv2.imshow("Received Video", video_frame)
    
    # @pc.on("icecandidate")
    # async def on_icecandidate():
    #     print("on_icecandidate")
    
    # await sio.emit("signal", {'sdp': pc.localDescription.sdp, 'type': pc.localDescription.type})
    # print("answer: ", answer)
    # jsonAnswer = json.dumps({"type": answer.type, "sdp": answer.sdp})
    # await sio.emit("acceptAnswer", jsonAnswer)

# @sio.on("call")
# async def call(request, candidate):
#     ip = candidate['candidate'].split(' ')[4]
#     port = candidate['candidate'].split(' ')[5]
#     protocol = candidate['candidate'].split(' ')[7]
#     priority = candidate['candidate'].split(' ')[3]
#     foundation = candidate['candidate'].split(' ')[0]
#     component = candidate['candidate'].split(' ')[1]
#     type = candidate['candidate'].split(' ')[7]
#     rtc_candidate = RTCIceCandidate(
#         ip=ip,
#         port=port,
#         protocol=protocol,
#         priority=priority,
#         foundation=foundation,
#         component=component,
#         type=type,
#         sdpMid=candidate['sdpMid'],
#         sdpMLineIndex=candidate['sdpMLineIndex']
#     )
#     await pc.addIceCandidate(rtc_candidate)
#     sio.emit("call")
#     # print("candidate: ", candidate["candidate"])
#     # rtc_candidate = RTCIceCandidate(candidate)
#     # print("rtc_candidate: ", rtc_candidate)
#     # pc.addIceCandidate(rtc_candidate)
    
@sio.on("message")
async def message(request, data):
    print("message")
    if data["type"] == "offer":
        try:
            offer = RTCSessionDescription(sdp=data['sdp'], type=data['type'])
        
            await pc.setRemoteDescription(offer)
            
            answer = await pc.createAnswer()
            
            await pc.setLocalDescription(answer)
            
            await pc.setRemoteDescription(offer)
            
            await sio.emit("message", {"sdp": pc.localDescription.sdp, "type": pc.localDescription.type})
            
        except ValueError:
            print("error:", ValueError)
            
    # if data["type"] == "candidate":
        # print("data: ", data)
        # print("candidate: ", candidate)
        # await pc.addIceCandidate(data)