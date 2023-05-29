import { styled } from "styled-components";


export const Container = styled.div`
  width: 100%;
  display: flex;

  .progress-0 {
    background-color: ${props => props.theme.gray['900']};
    border: 2px solid ${props => props.theme.gray['800']};
  }

  .progress-0-20 {
    background-color: ${props => props.theme.violet['900']};
    border: 2px solid ${props => props.theme.violet['800']};
  }

  .progress-20-40 {
    background-color: ${props => props.theme.violet['800']};
    border: 2px solid ${props => props.theme.violet['800']};
  }

  .progress-40-60 {
    background-color: ${props => props.theme.violet['700']};
    border: 2px solid ${props => props.theme.violet['500']};
  }

  .progress-60-80 {
    background-color: ${props => props.theme.violet['800']};
    border: 2px solid ${props => props.theme.violet['500']};
  }

  .progress-80-100 {
    background-color: ${props => props.theme.violet['500']};
    border: 2px solid ${props => props.theme.violet['400']};
  }

`

export const Week = styled.div`
  display: grid;
  grid-auto-flow: row;
  gap: 0.75rem;
  grid-template-rows: repeat(7, minmax(0, 1fr));
`
export const WeekDayName = styled.div`
  color: ${props => props.theme.gray['400']};
  font-size: 1.25rem;
  font-weight: 700;
  height: 2.5rem;
  width: 2.5rem;

  display: flex;
  align-items: center;
  justify-content: center;
`

export const Heatmap = styled.div`
  display: grid;
  grid-auto-flow: column;
  grid-template-rows: repeat(7, minmax(0, 1fr));
  gap: 0.75rem
`

export const DayToFill = styled.div`
  height: 2.5rem;
  width: 2.5rem;

  background-color: ${props => props.theme.gray['900']};
  border: 2px solid ${props => props.theme.gray['800']};
  border-radius: 0.5rem;

  opacity: 0.4;
  cursor: not-allowed;
`