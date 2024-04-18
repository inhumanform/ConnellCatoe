import React, { useState } from 'react'
import { FaBars, FaFacebook, FaTimes, FaInstagram } from 'react-icons/fa'
import { GiCarWheel } from 'react-icons/gi'
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
                    <li><a href="/"><Link onClick={handleClose} activeClass="active" to="power" spy={true} smooth={true} duration={500}>Home</Link></a></li>
                    <li><a href="/"><Link onClick={handleClose} activeClass="active" to="speed" spy={true} smooth={true} duration={500}>About</Link></a></li>
                    <li><a href="/"><Link onClick={handleClose} activeClass="active" to="handling" spy={true} smooth={true} duration={500}>In Production</Link></a></li>
                    <li><a href="/"><Link onClick={handleClose} activeClass="active" to="options" spy={true} smooth={true} duration={500}>Custom Leather</Link></a></li>
                    <li><a href="/"><Link onClick={handleClose} activeClass="active" to="contact" spy={true} smooth={true} duration={500}>Testimonials</Link></a></li>

                    <div className='mobile-menu'>
                        <button>Shop</button>
                        <button>Account</button>
                        <div className="social-icons">
                            <FaFacebook className='icon' />
                            <FaInstagram className='icon' />
                            <GiCarWheel className='icon' />
                        </div>
                    </div>

                </ul>

                <ul className='nav-menu hide'>
                    <li><a href="/">Shop</a></li>
                    <li><a href="/">Account</a></li>
                </ul>

                <div className="hamburger" onClick={handleNav} >
                    {nav ? (<FaTimes size={20} style={{ color: '#ffffff' }} />) : (<FaBars style={{ color: '#ffffff' }} size={20} />)}
                </div>

            </div>
        </div>
    )
}

export default Navbar
