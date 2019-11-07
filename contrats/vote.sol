pragma solidity >=0.4.22 <0.6.0;

contract Vote {

    address[4] public bureauVote;

    struct Personne {
        address bV;
        bool isVoted;
        address own;
    }

    Personne[] public personne;


    function addVoters(address bv, address pers) public returns (bool){
        personne.push(Personne(
            {
                bV : bv,
                isVoted: false,
                own: pers

            }
        ));

        return true;
    }
}