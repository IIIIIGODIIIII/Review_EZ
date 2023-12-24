import React from 'react';
import { BrowserRouter as Router, RouterProvider, createBrowserRouter } from 'react-router-dom';
import './App.css';
import Home from './pages/Home';
import Review from './pages/Review';

const router = createBrowserRouter([
  {
    path: '/',
    element:(
      <Home></Home>
    ),
  },{
    path:'/review',
    element:(
      <Review></Review>
    )
  }
])

function App() {
  return (
    <div className='App'>
      <RouterProvider router={router}></RouterProvider>
    </div>
  );
}

export default App;
