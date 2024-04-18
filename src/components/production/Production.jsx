


import React, { useState, useEffect } from 'react';
import './production.css';

const Production = () => {
    const [images, setImages] = useState([]);

    useEffect(() => {
        fetch('http://localhost:5555/image') 
            .then(response => response.json())
            .then(data => setImages(data))
            .catch(error => console.error('Error fetching images:', error));
    }, []);

    return (
        <div name='production' className='production'>
            <div className="container">
                <div className="top">
                    <h1>In Production</h1>
                </div>
                <div className="bottom">
                    {images.map((imageUrl, index) => (
                        <img key={index} src={imageUrl} alt={`Item ${index + 1}`} className="image" />
                    ))}
                </div>
            </div>
        </div>
    );
}

export default Production;
