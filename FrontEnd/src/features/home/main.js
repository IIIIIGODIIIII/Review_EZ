import React, { useState } from "react";
import { TextInput, Button, Spinner } from "flowbite-react";
import { useDispatch, useSelector } from "react-redux";
import { createWordCloudAsync, selectStatus } from "./mainSlice";
import { useNavigate } from "react-router-dom";
const Main = () => {
  const [url, setUrl] = useState("");
  const [link,setLink] = useState(false);
  const staus = useSelector(selectStatus);
  const handleChange = (e) => {
    setLink(isAmazonProductLink(e.target.value));
    setUrl(e.target.value);
  };
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const handleSubmit = async () => {
    // TODO: Submit the URL to your backend server for processing
    await dispatch(createWordCloudAsync(url));

      // Navigation logic after the dispatch is successful
      navigate('/review');
    // {<Navigate to='/review' replace = {true}></Navigate>}
    // console.log(url);

  };

  const isAmazonProductLink = (url)=> {
    // Define a regular expression for Amazon product links
    const amazonProductLinkPattern = /^https?:\/\/(www\.)?amazon\.([a-z]{2,3}\.)?[a-z]{2,3}\/[a-zA-Z0-9-]+\/dp\/[a-zA-Z0-9]+(\/|\?)?.*$/;
  
    // Test the provided URL against the pattern
    return amazonProductLinkPattern.test(url);
  }

  return (
    <div
      className="bg-cover"
      style={{
        backgroundImage: `url(${process.env.PUBLIC_URL}/img/bg.jpg)`,
        height: "100vh",
      }}
    >
      {staus==='idle'?<div className="container flex flex-col items-center">
        <div className="my-8 p-8 text-5xl text-white font-bold tracking-wide">
          <h1>Please Provide the Product Link</h1>
        </div>
        <div className="my-8 p-8 text-xl text-white font-bold ">
          <h1>
            Grab the product link which can be found in the search bar of your
            browser
          </h1>
        </div>
        <div className="max-w-2xl" style={{ width: "90vw" }}>
          <TextInput
            id="username3"
            placeholder="https://www.amazon.in/Logitech-B170-Wireless-Mouse-Black/dp/B01J0XWYKQ/?_encoding=UTF8"
            addon="Amazon Product Link"
            required
            onChange={handleChange}
          />
        </div>
        <div className="my-8">
        {<Button size="xl"  pill onClick={handleSubmit} disabled={!link}>
        Generate Image
      </Button>}
        </div>
      </div>:<div className="flex flex-wrap items-center gap-2">
      <div className="my-8 p-8 text-5xl text-white font-bold tracking-wide">
          <h1>We are Genrating your word cloud</h1>
        </div>
        <div className="my-8 p-8 text-xl text-white font-bold ">
        <Spinner color="success" aria-label="Extra large spinner example" size="xl" />
        </div>
      </div>}
    </div>
  );
};

export default Main;
