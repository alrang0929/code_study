import React, { useEffect } from "react";

function App(props) {
const [value, setValue] = useState(false);
useEffect(() => {
console.log("hello useEffect!");

}, [])

  return (
    <>
    <h1>useEffect</h1>

    </>
  );
}

export default App;
