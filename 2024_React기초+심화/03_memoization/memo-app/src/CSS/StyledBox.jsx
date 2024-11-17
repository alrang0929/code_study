import styled from 'styled-components'
export const StyledBox = styled.div`
    width: 100px;
    height: 100px;
    color: #fff;
    background-color: ${({bgcolor})=> bgcolor };
    display: flex;
    justify-content: center;
    align-items: center;
`