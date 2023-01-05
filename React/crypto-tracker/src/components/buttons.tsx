import styled from 'styled-components';

function Btn({ txt, onClick }: IBtn) {
  return <StyledBtn onClick={onClick}>{txt}</StyledBtn>;
}

const StyledBtn = styled.button`
  padding: 10px 15px;
  color: ${(props) => props.theme.textColor};
  background-color: ${(props) => props.theme.bgColor};
  border: 1px solid;
  border-radius: 10px;
`;

interface IBtn {
  txt: string;
  onClick?: () => void;
}

export default Btn;
