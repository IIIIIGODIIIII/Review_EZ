'use client';
import React from 'react'
import { Button, DarkThemeToggle, Flowbite, Navbar } from 'flowbite-react';


function Nav() {
  return (
    <Flowbite>
    <Navbar fluid rounded className='bg-neutral-200'>
      <Navbar.Brand href="https://flowbite-react.com">
        {/* <img src="/favicon.svg" className="mr-3 h-6 sm:h-9" alt="Flowbite React Logo" /> */}
        <span className="self-center whitespace-nowrap text-xl font-semibold dark:text-white">ReviewViz</span>
      </Navbar.Brand>
      <div className="flex md:order-2">
        <Button className='mx-4'>Get started</Button>
        <DarkThemeToggle />
        <Navbar.Toggle />
      </div>
      <Navbar.Collapse>
        <Navbar.Link href="#" active>
          Home
        </Navbar.Link>
        <Navbar.Link href="#">About</Navbar.Link>
        <Navbar.Link href="#">Services</Navbar.Link>
        <Navbar.Link href="#">Pricing</Navbar.Link>
        <Navbar.Link href="#">Contact</Navbar.Link>
      </Navbar.Collapse>
    </Navbar>
    </Flowbite>
  )
}

export default Nav
