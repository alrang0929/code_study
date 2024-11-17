import { useState } from "react";

const useInput = () => {
    // value를 useState로 관리
    const [value,setValue] = useState("");

    // handler 로직
    const handler = (e) => {
        setValue(e.target.value);
    };//handler

    return [value, handler]

};

export default useInput;