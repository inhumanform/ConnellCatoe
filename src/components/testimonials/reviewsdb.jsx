import Item from './item'

function Item(){
    return (
        <li>
            <h1>{review.item}</h1>
            <h2>{review.customer}</h2>
            <h2>{review.text}</h2>
        </li>
    )
}

export default Item;