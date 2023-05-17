import { api } from "../api/axios";
import { CheckHabitRequest } from "../interfaces/api";

export class DayService {


  static async listDays(){
    const response = await api.get('/days')
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