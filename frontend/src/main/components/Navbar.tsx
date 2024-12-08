function Navbar(props: { name: string }) {
    return <div className={"w-full px-10 h-32 flex items-center"}>
        <div className={"flex flex-col content-center w-56"}>
            <h1 className={"text-2xl text-indigo-400 start-0"}>Bienvenida</h1>
            <h2 className={"text-xl text-end"}>{props.name}</h2>
        </div>
    </div>;
}

export default Navbar