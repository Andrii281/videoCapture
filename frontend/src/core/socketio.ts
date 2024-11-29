import io from "socket.io-client";

// export const appSocket = io("http://127.0.0.1:8000", { transports: ["websocket"] });
export const appSocket = io("http://127.0.0.1:8000");
