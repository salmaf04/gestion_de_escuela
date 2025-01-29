export type ProfesorEspGetDB = {
    "id": string,
    "name": string,
    "specialty": string,
    "mean": string,
    "state": string,
}

export type FiltrodeMantenimientoGetDB = [
    {
        classroom_id: string,
        other: number,
        teaching_material: number,
        technological_mean: number
    }[],
    {
        "total maintenances after two years": number
    }
];