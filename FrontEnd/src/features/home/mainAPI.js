export function createWordCloud(url) {
  return new Promise(async (resolve) =>{
    console.log('url :>> ', url);
    const response = await fetch(`http://localhost:8080/word?url=${encodeURIComponent(url)}`);
    // const data = await response.json();
    // console.log('data :>> ', data);
    resolve(response);
  }
  );
}