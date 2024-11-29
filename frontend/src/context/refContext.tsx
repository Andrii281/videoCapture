import { createContext, useContext, PropsWithChildren, useState } from "react";

import { peerConnection } from "~/core/peerConnection";

interface IVideoStreamContext {
  videoStream: MediaStream | null;
  isRecording: boolean;
  startRecording: () => void;
  stopRecording: () => void;
}

const VideoStreamContext = createContext<IVideoStreamContext>({} as IVideoStreamContext);

export const useVideoStreamContext = (): IVideoStreamContext => {
  return useContext(VideoStreamContext);
};

export const VideoStreamProvider = ({ children }: PropsWithChildren) => {
  const [videoStream, setVideoStream] = useState<MediaStream | null>(null);
  const [isRecording, setIsRecording] = useState<boolean>(false);

  const startRecording = async () => {
    await navigator.mediaDevices.getUserMedia({ video: true, audio: false }).then((strem) => {
      setVideoStream(strem);
      strem.getTracks().forEach((track) => peerConnection.addTrack(track, strem));
    });
    setIsRecording(true);
  };

  const stopRecording = () => {
    if (videoStream) {
      videoStream.getTracks().forEach((track) => {
        track.stop();
      });
      setVideoStream(null);
    }
    setIsRecording(false);
  };

  return (
    <VideoStreamContext.Provider value={{ videoStream, isRecording, startRecording, stopRecording }}>
      {children}
    </VideoStreamContext.Provider>
  );
};
