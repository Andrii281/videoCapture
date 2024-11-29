// const configuration = {
//   iceServers: [
//     { urls: "stun:stun.l.google.com:19302" },
//     { urls: "turn:numb.viagenie.ca", credential: "muazkh", username: "webrtc@live.com" },
//   ],
// };

const configuration = {
  sdpSemantics: "unified-plan",
  iceServers: [{ urls: ["stun:stun.l.google.com:19302"] }],
};

export const peerConnection = new RTCPeerConnection(configuration);
