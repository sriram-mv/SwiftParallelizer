echo $1
python files_into_queue.py $1
python create_container.py test:tester testing $1
python multiprocessing_queue_in.py $1
python objectstore_into_queue.py test:tester testing $1
python multiprocessing_queue_out.py $1
cat part* > $1
rm -rf part*
IP=$0
IP=(${IP//./ });
rm -rf /home/sriram/SpecialProblem/Objects/${IP[0]}

