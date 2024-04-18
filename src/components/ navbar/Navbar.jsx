import React, { useState } from 'react'
import './NavbarStyles.css'
import { Link } from 'react-scroll'


const Navbar = () => {
    const [nav, setNav] = useState(false)
    const [slide, setSlide] = useState(false)

    const handleNav = () => {
        setNav(!nav)
        setSlide(!slide)
    }

    const handleClose = () => {
        setNav(!nav)
    }

    return (
        <div className='navbar'>
            <div className="container">
                <div className={slide ? 'logo slide-right' : 'logo'}>
                    <h3>catoe | connell</h3>
                    {/* <h4>to a fault.</h4> */}
                </div>
                <ul className={nav ? 'nav-menu active' : 'nav-menu'}>
                    <li><a href="/"><Link onClick={handleClose} activeClass="active" to="home" spy={true} smooth={true} duration={500}>Home</Link></a></li>
                    <li><a href="/"><Link onClick={handleClose} activeClass="active" to="about" spy={true} smooth={true} duration={500}>About</Link></a></li>
                    <li><a href="/"><Link onClick={handleClose} activeClass="active" to="production" spy={true} smooth={true} duration={500}>In Production</Link></a></li>
                    <li><a href="/"><Link onClick={handleClose} activeClass="active" to="testimonials" spy={true} smooth={true} duration={500}>Testimonials</Link></a></li>
                    <li><a href="/"><Link onClick={handleClose} activeClass="active" to="contact" spy={true} smooth={true} duration={500}>Custom Leather</Link></a></li>
                    
                </ul>
            </div>
        </div>
    )
}

export default Navbar
