export type AulaDB = {
        name: string
        hourly_load: number
        study_program: number
        classroom_id: string
    }

export type AulaGetResponse = AulaDB[]