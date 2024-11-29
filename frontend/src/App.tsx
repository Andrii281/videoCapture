import { useEffect } from "react";

import { Layout } from "./layout/Layout";
import { videoStreamApi } from "./streamApi/videoStream";

function App() {
  useEffect(() => {
    // videoStreamApi.signal();
    videoStreamApi.message();
  }, []);

  return (
    <>
      <Layout />
    </>
  );
}

export default App;
