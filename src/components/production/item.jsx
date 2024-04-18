function Item({items}){
    return (
        <div>
            <img src={items.image}/>
            <h1>{items.name}</h1>
        </div>
    )
}

export default Item;