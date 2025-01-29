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

export type CostoPromedioGetDB = {
    "average_cost": string,
    "mean_id": string,
    "mean_name": string,
}

export type ValoracionPromediodeProfesorGetDB =  {
    name: string;
    average_valoration: number;
    subjects: string[];
}

export type ValoracionPromediodeEstudianteGetDB = {
    name: string;
    student_id: string;
    teacher_name: string;
    teacher_valoration: number | null;
}

export type SalariosdeProfesoresGetDB = {
    name: string;
    valorations: number[];
    date: string;
    means: boolean;
}