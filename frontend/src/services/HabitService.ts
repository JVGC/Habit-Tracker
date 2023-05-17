import { api } from "../api/axios"

interface CreateNewHabitRequest {
  title: string;
  startAt: string;
}
export class HabitService {

  static async createNewHabit({ title, startAt }: CreateNewHabitRequest){
    const response = await api.post('/habits/add', {
      name: title,
      start_at: startAt
    })
    return response.data

  }
}