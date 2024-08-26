#if !defined(BLOCK_ID_MAPPING)
#define BLOCK_ID_MAPPING
// This file was automatically generated by block_wrangler


struct Sway {int value;};
const Sway Sway_NONE = Sway(0);
const Sway Sway_TOP = Sway(1);
const Sway Sway_BOTTOM = Sway(2);
const Sway Sway_FULL = Sway(3);
const Sway Sway_FLOATING = Sway(4);
const Sway Sway_HANGING = Sway(5);
Sway SwayType(int id) {
	if (id == 28 || id == 33)
		return Sway_TOP;
	if (id == 27 || id == 32)
		return Sway_BOTTOM;
	if (id == 31)
		return Sway_FULL;
	if (id == 30)
		return Sway_FLOATING;
	if (id == 11 || id == 29)
		return Sway_HANGING;
	return Sway_NONE;
}


bool IsCrops(int id) {
	return id == 27 || id == 28;
}


bool IsWater(int id) {
	return id == 26;
}


int GetEmissivity(int id) {
	if (id == 25)
		return 1;
	if (id == 24)
		return 2;
	if (id == 23)
		return 3;
	if (id == 22)
		return 4;
	if (id == 21)
		return 5;
	if (id == 20)
		return 6;
	if (id == 19)
		return 7;
	if (id == 18)
		return 8;
	if (id == 17)
		return 9;
	if (id == 16)
		return 10;
	if (id == 15)
		return 11;
	if (id == 14)
		return 12;
	if (id == 13)
		return 13;
	if (id == 12)
		return 14;
	if (id == 10 || id == 11)
		return 15;
	return 0;
}


#endif // BLOCK_ID_MAPPING