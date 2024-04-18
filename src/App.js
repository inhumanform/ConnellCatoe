import React from 'react'
import Contact from './components/contact/Contact';
import Production from './components/production/Production';
import Navbar from './components/ navbar/Navbar'
import Testimonials from './components/testimonials/Testimonials';
import Home from './components/home/Home'
import About from './components/about/About';

function App() {
  return (
    <>
      <Navbar />
      <Home />
      <About />
      <Production />
      <Testimonials />
      <Contact />
    </>
  );
}

export default App;
