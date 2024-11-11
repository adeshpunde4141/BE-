// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    
    // Structure to represent a student
    struct Student {
        uint256 id;
        string name;
        uint8 age;
        string course;
    }
    
    // Array to store student data
    Student[] public students;

    // Event to log student addition
    event StudentAdded(uint256 id, string name, uint8 age, string course);

    // Add a new student to the array
    function addStudent(uint256 _id, string memory _name, uint8 _age, string memory _course) public {
        Student memory newStudent = Student({
            id: _id,
            name: _name,
            age: _age,
            course: _course
        });
        students.push(newStudent);
        
        // Emit an event for the added student
        emit StudentAdded(_id, _name, _age, _course);
    }

    // Get the number of students
    function getStudentCount() public view returns (uint256) {
        return students.length;
    }

    // Retrieve a student's data by index
    function getStudent(uint256 index) public view returns (uint256, string memory, uint8, string memory) {
        require(index < students.length, "Index out of bounds.");
        Student memory student = students[index];
        return (student.id, student.name, student.age, student.course);
    }

    // Receive function to handle plain ether transfers
    receive() external payable {}

    // Fallback function to handle calls with data or undefined functions
    fallback() external payable {}

    // Function to get the contract balance
    function getContractBalance() public view returns (uint256) {
        return address(this).balance;
    }
}