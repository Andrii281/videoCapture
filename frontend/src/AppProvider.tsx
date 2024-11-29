import { PropsWithChildren } from "react";

import { VideoStreamProvider } from "./context/VideoSteamContext";

export const AppProvider = ({ children }: PropsWithChildren) => {
  return <VideoStreamProvider>{children}</VideoStreamProvider>;
};
