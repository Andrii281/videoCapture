export const handleNewICECandidateMsg = (candidate, peerConnection: RTCPeerConnection) => {
  const iceCandidate = new RTCIceCandidate(candidate);
  peerConnection.addIceCandidate(iceCandidate);
};
