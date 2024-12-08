import ScreenType, {Screens} from "../types.ts";

interface Props {
    actualScreen: ScreenType,
    setActualScreen: (screen: ScreenType) => void
}

function Sidebar({actualScreen, setActualScreen}: Props) {
    return <div className={"w-1/6 flex flex-col justify-center items-center"}>
        <div className={' flex flex-col items-center justify-center gap-10'}>
            {
                Object.values(Screens).map((screen: ScreenType) => {
                    return (
                        <div key={screen.title} onClick={() => setActualScreen(screen)}
                             className={`transition-all cursor-pointer font-semibold size-24 space-y-1 justify-center rounded-xl flex flex-col items-center ${actualScreen === screen ? 'bg-indigo-100' : ''}`}>
                            <img src={screen.icon} alt={screen.title} className={'w-10 h-10'}/>
                            <p className={'text-xs text-indigo-950'}>{screen.title}</p>
                        </div>)
                })
            }

        </div>
    </div>;
}

export default Sidebar