export type EstudianteGetDB =
    {   id : string,
        name: string,
        age: 0,
        email: string,
        extra_activities: true,
        username: string,
        password: string
    }

export type EstudianteGetResponse = {
    [index: string]: EstudianteGetDB
}