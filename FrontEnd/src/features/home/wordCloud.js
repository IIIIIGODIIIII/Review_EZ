import React, { useEffect, useState } from "react";
import { useSelector } from 'react-redux'
import { selectWordCloud } from "./mainSlice";
const WordCloud = () => {
  const [imageSrc, setImageSrc] = useState("");
  const response = useSelector(selectWordCloud);
  const fetchImage = async ()=>{
    // const imageData = await response.arrayBuffer();
    setImageSrc(response)
  }
    useEffect(()=>{fetchImage()},[selectWordCloud])
  return (
    <div
      className="bg-cover"
      style={{
        backgroundImage: `url(${process.env.PUBLIC_URL}/img/bg.jpg)`,
        height: "100vh",
      }}
    >
      <div className="container flex flex-col items-center">
       <img className="my-8" src={imageSrc} alt="Fetched Image"></img>
      </div>
    </div>
  );
};

export default WordCloud;
