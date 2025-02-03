export type IEstudianteCreateDB = {
    name: string,
    age: number,
    lastname: string,
    email: string,
    extra_activities: boolean,
    username: string,
    password?: string,
    course_id: string,
}