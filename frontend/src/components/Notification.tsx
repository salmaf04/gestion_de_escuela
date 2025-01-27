interface Props {
    title: string
    message: string
    className?: string
    onClick: () => void
}

export default function Notification({title, message, className, onClick}: Props) {
    return (
        <div id={'alert'} className={'fixed z-30 flex inset-0 justify-center p-4 text-white transition-all'} onClick={
            ()=>{onClick()}
        }>
            <div className={`bg-indigo-300 flex flex-col w-1/5 rounded-lg py-1 px-4 h-fit ${className} animate-slide-down`}>
                <h1 className={'font-semibold text-indigo-950'}>{title}</h1>
                <p className={'text-indigo-950 text-sm'}>{message}</p>
            </div>
        </div>)
}