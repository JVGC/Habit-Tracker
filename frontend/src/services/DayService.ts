import { api } from "../api/axios";
import { CheckHabitRequest } from "../interfaces/api";
import { Day } from "../interfaces/models";

export class DayService {


  static async listDays():Promise<Day[]>{
    const response = await api.get<Day[]>('/days')
    return response.data
  }

  static async checkHabit({habit, date}: CheckHabitRequest){
    const response = await api.put('/days/check', {
      habit,
      date
    })
    return response.data
  }
}