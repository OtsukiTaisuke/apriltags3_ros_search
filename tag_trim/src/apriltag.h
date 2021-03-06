#ifndef APRILTAG_H
#define APRILTAG_H

#include <eigen3/Eigen/Dense>
#include <iostream>
class Apriltag{
	public:
		Apriltag() :pose(0,0,0),speed(0,0,0),q(0,0,0,1),vq(0,0,0,1){};
//		Apriltag(unsigned int id, const double xx, const double yy, const double zz, const Eigen::Quaterniond qq) :x(xx),y(yy),z(zz),vx(0),vy(0),vz(0),q(qq),vq(0,0,0,1){};
		Apriltag(unsigned int iid, Eigen::Vector3d ppos,
                const Eigen::Quaterniond qq,double ssize) :id(iid),pose(ppos),speed(0,0,0),q(qq),vq(0,0,0,1),size(ssize){};
		~Apriltag(){};
        void update(unsigned int iid,Eigen::Vector3d ppos,
        Eigen::Quaterniond qq,Eigen::Vector3d pre_pos,
        Eigen::Quaterniond pre_q);
		void reset(unsigned int iid,Eigen::Vector3d ppos,Eigen::Quaterniond qq);
		void reset_velocity();
		Eigen::Quaterniond getQuaterniond();
		double getSize();
		double getX();
		double getY();
		double getZ();
		double getVx();
		double getVy();
		double getVz();
		double getAx();
		double getAy();
		double getAz();
	private:
		unsigned int id ;
		double size; //m
		//double x,y,z;
		//double vx,vy,vz;

		Eigen::Vector3d pose; // (x y z)
		Eigen::Vector3d speed; // (x y z)
		Eigen::Vector3d accel; // (x y z)
		//double ax,ay,az ;//acc
		Eigen::Quaterniond q;//Quartation (w, x, y, z)
		Eigen::Quaterniond vq;//Quartation (w, x, y, z)

		Eigen::Vector3d obj_speed; // (x y z)
		Eigen::Vector3d pre_speed; // (x y z)
		Eigen::Vector3d prepre_speed; // (x y z)

		void update_pose(Eigen::Vector3d ppos, Eigen::Quaterniond qq);
	//	void update_velocity(double xx, double yy, double zz, Eigen::Quaterniond qq);
        void update_velocity(Eigen::Vector3d ppos,
                Eigen::Quaterniond qq,Eigen::Vector3d pre_pos,
                Eigen::Quaterniond pre_q);
		void update_accel(Eigen::Vector3d ppos, Eigen::Quaterniond qq);
};

#endif //APRILTAG_H
