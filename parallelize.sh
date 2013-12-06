python files_into_queue.py $1 $2
python create_container.py test:tester testing $1
python multiprocessing_queue_in.py $1 $3
python objectstore_into_queue.py test:tester testing $1
python multiprocessing_queue_out.py $1 $3
cat part* > $1
rm -rf part*
IP=$1
IP=(${IP//./ });
rm -rf /home/sriram/SpecialProblem/Objects/${IP[0]}
rm -rf swift_xuath.conf
