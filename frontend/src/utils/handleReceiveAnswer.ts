export const handleReceiveAnswer = async (sdp: string, type: RTCSdpType, peerConnection: RTCPeerConnection) => {
  const remoteDesc = new RTCSessionDescription({ sdp: sdp, type: type });
  await peerConnection.setRemoteDescription(remoteDesc);
};
