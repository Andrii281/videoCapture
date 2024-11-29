import { appSocket } from "~/core/socketio";

export const handleReceiveOffer = (offer, peerConnection: RTCPeerConnection) => {
  peerConnection
    .setRemoteDescription(new RTCSessionDescription(offer))
    .then(() => peerConnection.createAnswer())
    .then((answer) => peerConnection.setLocalDescription(answer))
    .then(() => appSocket.emit("signal", { type: "answer", answer: peerConnection.localDescription }));
};
