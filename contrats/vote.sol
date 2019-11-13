pragma solidity >=0.4.22 <0.6.0;

contract Vote {

    address[4] public bureauVote;

    struct Personne {
        address bV;
        address own;
        bool isVoted;
        address bVwhere;
    }


    Personne[] public personne;


    function addVoters(address bv, address pers) public returns (bool){
        personne.push(Personne(
            {
                bV : bv,
                isVoted: false,
                own: pers,
                bVwhere: pers

            }
        ));

        return true;
    }


    function helloWorld() public pure returns (string memory){
        return "Hello World";
    }


    function voting(address pers, address bVplace) public returns (uint){
        for (uint i = 0; i < personne.length; i++){
            if (pers == personne[i].own){
                if (personne[i].isVoted == false){
                    personne[i].isVoted = true;
                    personne[i].bVwhere = bVplace;
                    return 1;
                }
                else{
                    return 0;
                }
            }
        }
        return 404;
    }
}