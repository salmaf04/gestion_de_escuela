export type IEstudianteCreateDB = {
    name: string,
    age: number,
    email: string,
    extra_activities: boolean,
    username: string,
    password?: string,
    course_id: string,
}