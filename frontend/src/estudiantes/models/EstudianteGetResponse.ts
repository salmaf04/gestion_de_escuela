export type EstudianteDB = {
        name: string
        hourly_load: number
        study_program: number
        classroom_id: string
    }

export type EstudianteGetResponse = EstudianteDB[]