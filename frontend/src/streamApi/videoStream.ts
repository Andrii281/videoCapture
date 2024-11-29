import { peerConnection } from "~/core/peerConnection";
import { appSocket } from "~/core/socketio";
import { handleNewICECandidateMsg } from "~/utils/handleNewICECandidateMsg";
import { handleReceiveAnswer } from "~/utils/handleReceiveAnswer";
import { handleReceiveOffer } from "~/utils/handleReceiveOffer";

interface IMessage {
  type: string;
  candidate: null | string;
  sdpMid?: null | string;
  sdpMLineIndex?: number | null;
}

export const videoStreamApi = {
  sendMessage: () => {
    const result = appSocket.emit("msg", { message: "msg" });
    console.log("result: ", result);
  },
  makeCall: async () => {
    peerConnection.addTransceiver("video", { direction: "recvonly" });
    const offer = await peerConnection.createOffer();
    await peerConnection.setLocalDescription(offer);
    // peerConnection.onicecandidate = (e) => {
    //   console.log("onicecandidate");
    //   const message: IMessage = {
    //     type: "candidate",
    //     candidate: null,
    //   };
    //   if (e.candidate) {
    //     message.candidate = e.candidate.candidate;
    //     message.sdpMid = e.candidate.sdpMid;
    //     message.sdpMLineIndex = e.candidate.sdpMLineIndex;
    //   }
    //     appSocket.emit("message", message);
    // };

    // peerConnection.ontrack = (track) => {
    //   console.log("track: ", track);
    // };

    appSocket.emit("message", { type: offer.type, sdp: offer.sdp });
  },

  message: async () => {
    appSocket.on("message", async (e) => {
      console.log("message");
      //   const event = JSON.parse(e);
      console.log("peerConnection.local: ", peerConnection.localDescription);
      console.log("peerConnection.remote: ", peerConnection.remoteDescription);
      switch (e.type) {
        case "answer":
          //   handleReceiveAnswer(event.sdp, event.type, peerConnection);
          await peerConnection.setRemoteDescription(new RTCSessionDescription(e));
      }
    });
  },
};
