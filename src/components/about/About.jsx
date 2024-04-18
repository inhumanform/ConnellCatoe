// import React from 'react'
// import './about.css'

// const About = () => {
//     return (
//         <div name='about' className='about'>
//             <div className="container">
//                 <div className="top">
//                     <h1>What does quality mean to us?</h1>
//                 </div>
//                 <p>Every aspect of our leatherwork is orchestrated by a single, dedicated craftswoman. Every piece is sourced ethically, and selected by hand. When we make a piece there are no machines, no factories, and no compromises. </p>
//                 <div className="bottom">
//                     <button className="btn btn-dark">Drive</button>
//                     <button className="btn">Ride</button>
//                 </div>
//             </div>
//         </div>
//     )
// }

// export default About



import React from 'react';
import './about.css';

const About = () => {
    return (
        <div name='about' className='about'>
            <div className="image"></div>
            <div className="text">
                <div className="container">
                    <div className="top">
                        <h1>What does quality mean to us?</h1>
                    </div>
                    <p>Every aspect of our leatherwork is orchestrated by a single, dedicated craftswoman. Every piece is sourced ethically, and selected by hand. When we make a piece there are no machines, no factories, and no compromises. </p>

                </div>
            </div>
        </div>
    );
}

export default About;