import { api } from "@/api/axios"
import { CreateNewHabitRequest, ListHabitsRequest } from "@/interfaces/api"
import { Habit } from "@/interfaces/models"

export class HabitService {

  static async createNewHabit({ title, startAt }: CreateNewHabitRequest): Promise<Habit>{
    const response = await api.post('/habits/add', {
      name: title,
      start_at: startAt
    })
    return response.data

  }

  static async listHabits({date}: ListHabitsRequest): Promise<Habit[]>{
    const response = await api.get<Habit[]>('/habits', {
      params:{
        date
      }
    })
    return response.data
  }
}