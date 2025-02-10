import {RolesEnum} from "../api/RolesEnum.ts";

export function getQueryParamsFromObject(obj: any): string {
    return "?"+ Object.keys(obj)
        .map(key => `${key}=${obj[key]}`)
        .join('&');
}
export function reverseDate(date: string): string {
    return date.split('-').reverse().join('-')
}

export const rolesDisplayParser = {
    [RolesEnum.ADMIN]: 'Administrador',
    [RolesEnum.TEACHER]: 'Profesor',
    [RolesEnum.STUDENT]: 'Estudiante',
    [RolesEnum.SECRETARY]: 'Secretaria',
    [RolesEnum.DEAN]: 'Decano'
}