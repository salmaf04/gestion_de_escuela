
import { Label, Listbox, ListboxButton, ListboxOption, ListboxOptions } from '@headlessui/react'
import { ChevronUpDownIcon } from '@heroicons/react/16/solid'
import { CheckIcon } from '@heroicons/react/20/solid'
import {ISelect} from "../types/ISelect.ts";
import {useController, UseControllerProps} from "react-hook-form";
import {useEffect, useState} from "react";


interface Props{
    data: ISelect[],
    label?: string,
    labelClassName?: string,
    defaultValue?: ISelect,
}
export default function Select(props: UseControllerProps & Props) {
    const { field } = useController(props);
    const {data, label, labelClassName, defaultValue} = props
    const [selected, setSelected] = useState<ISelect | null>(null);

    useEffect(() => {
        const current = data.find(
            (item) => item.id === defaultValue || field.value === item.id
        );
        if (current) {
            setSelected(current);
            field.onChange(current.id);
        }
    }, [defaultValue]);
    return (
        <Listbox value={selected} onChange={(e)=>{
            setSelected(e);
            field.onChange(e?.id);
        }}
        defaultValue={field.value}

        >
            <Label className={labelClassName}>{label}</Label>
            <div className="relative">
                <ListboxButton {...field} className="grid w-full cursor-default grid-cols-1 rounded-md bg-white py-1.5 pl-3 pr-2 text-left text-gray-900 outline outline-1 -outline-offset-1 outline-gray-300 focus:outline focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm/6">
                    <span className="col-start-1 row-start-1 truncate pr-6">{selected?.name ?? "Seleccione"}</span>
                    <ChevronUpDownIcon
                        aria-hidden="true"
                        className="col-start-1 row-start-1 size-5 self-center justify-self-end text-gray-500 sm:size-4"
                    />
                </ListboxButton>

                <ListboxOptions
                    transition
                    className="absolute z-10 mt-1 max-h-60 w-full overflow-auto rounded-md bg-white py-1 text-base shadow-lg ring-1 ring-black/5 focus:outline-none data-[closed]:data-[leave]:opacity-0 data-[leave]:transition data-[leave]:duration-100 data-[leave]:ease-in sm:text-sm"
                >
                    {data.map((item) => (
                        <ListboxOption
                            key={item.id}
                            value={item}
                            className="group relative cursor-default select-none py-2 pl-3 pr-9 text-gray-900 data-[focus]:bg-indigo-600 data-[focus]:text-white data-[focus]:outline-none"
                        >
                            <span className="block truncate font-normal group-data-[selected]:font-semibold">{item.name}</span>

                            <span className="absolute inset-y-0 right-0 flex items-center pr-4 text-indigo-600 group-[&:not([data-selected])]:hidden group-data-[focus]:text-white">
                <CheckIcon aria-hidden="true" className="size-5" />
              </span>
                        </ListboxOption>
                    ))}
                </ListboxOptions>
            </div>
        </Listbox>
    )
}
